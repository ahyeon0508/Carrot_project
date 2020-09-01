package org.techtown.kotlincarrot

import android.os.Bundle
import android.view.Gravity
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import getUnsafeOkHttpClient
import kotlinx.android.synthetic.main.activity_main.*
import org.techtown.kotlincarrot.DataModel.ActionDataClass
import org.techtown.kotlincarrot.DataModel.DataClass
import org.techtown.kotlincarrot.DataModel.WeatherDataClass
import org.techtown.kotlincarrot.Request.RequestApi
import org.techtown.kotlincarrot.Request.RequestWeatherApi
import retrofit2.Call
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory
import java.time.ZoneId
import java.time.ZonedDateTime
import java.time.format.TextStyle
import java.util.*


class MainActivity : AppCompatActivity() {

    companion object {
        var BASE_URL = "https://carrot-project.herokuapp.com/"
        var BASE_URL_WEATHER = "http://api.openweathermap.org/data/2.5/"
    }

    val retrofit = Retrofit.Builder()
        .baseUrl(BASE_URL)
        .client(getUnsafeOkHttpClient())
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    val retrofitWeather = Retrofit.Builder()
        .baseUrl(BASE_URL_WEATHER)
        .addConverterFactory(GsonConverterFactory.create())
        .build()

    val service = retrofit.create(RequestApi::class.java)
    val response = service.getAllPosts()
    val response3 = service.getAllPostsAction()

    val service2 = retrofitWeather.create(RequestWeatherApi::class.java)
    val response2 = service2.getWeatherData()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        getCarrotInfo()
        getWeatherInfo()
        getActionInfo()
    }

    private fun getCarrotInfo() {
        response.enqueue(object : retrofit2.Callback<DataClass> {
            override fun onFailure(call: retrofit2.Call<DataClass>, t: Throwable) {
                t.printStackTrace()
            }

            override fun onResponse(call: Call<DataClass>, response: Response<DataClass>) {
                if (response.isSuccessful) {
                    houseView.setText("당근 하우스")
                    temperatureView.setText(response.body()?.temperature.toString() + "°C")
                    wetnessInfoView.setText("다음 물주기까지")
                    wetnessView.setText(String.format("%.0f", response.body()?.wetness) + "일")

                    response.body()?.end_status?.let { endStatus(it) }
                }
            }
        })
    }

    private fun getWeatherInfo() {
        response2.enqueue(object : retrofit2.Callback<WeatherDataClass> {
            override fun onFailure(call: retrofit2.Call<WeatherDataClass>, t: Throwable) {
                t.printStackTrace()
            }

            override fun onResponse(call: retrofit2.Call<WeatherDataClass>, response2: Response<WeatherDataClass>) {
                val temperature = response2.body()?.main?.temp?.minus(273.0)
                tempView.setText(String.format("%.1f°C", temperature))

                val dateAndtime: ZonedDateTime = ZonedDateTime.now((ZoneId.of("Asia/Seoul")))
                dateView.setText(dateAndtime.monthValue.toString() + "/" + dateAndtime.dayOfMonth.toString() + " ")

            }
        })
    }

    private fun getActionInfo() {
        response3.enqueue(object : retrofit2.Callback<ActionDataClass> {
            override fun onFailure(call: retrofit2.Call<ActionDataClass>, t: Throwable) {
                t.printStackTrace()
            }

            override fun onResponse(call: retrofit2.Call<ActionDataClass>, response3: Response<ActionDataClass>) {
                response3.body()?.code?.let { actionStatus(it) }
            }
        })
    }

    private fun endStatus(end_status: Int) {
        val carrotStatus : String

        when (end_status) {
            100 -> carrotStatus = "당근 키우기 종료"
            300 -> carrotStatus = "흰가루병"
            301 -> carrotStatus = "검은잎마름병"
            else -> carrotStatus =""
        }

        val toast = Toast.makeText(this@MainActivity, carrotStatus, Toast.LENGTH_LONG)
        toast.setGravity(Gravity.TOP, 0, 0)
        toast.show()
    }

    private fun actionStatus(action_status: Int){
        when(action_status){
            0 -> actionView.setText("물주기")
            1 -> actionView.setText("온도올리기")
            2 -> actionView.setText("온도내리기")
            3 -> actionView.setText("대기")
        }
    }
}
