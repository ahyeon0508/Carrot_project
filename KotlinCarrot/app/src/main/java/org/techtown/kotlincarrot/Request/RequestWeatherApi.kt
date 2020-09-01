package org.techtown.kotlincarrot.Request

import org.techtown.kotlincarrot.DataModel.WeatherDataClass
import retrofit2.Call
import retrofit2.http.Body
import retrofit2.http.GET
import retrofit2.http.Query


interface RequestWeatherApi {
    @GET("weather?lat=37.476200&lon=126.973154&APPID=0cbcc07997dfa6112e5245bfee24ae69")
    fun getWeatherData() : Call<WeatherDataClass>
}