
package org.techtown.kotlincarrot.Request

import org.techtown.kotlincarrot.DataModel.ActionDataClass
import org.techtown.kotlincarrot.DataModel.DataClass
import retrofit2.Call
import retrofit2.http.GET

interface RequestApi {

    @GET("carrots/current-status/?format=json")
    //current-status
    fun getAllPosts() : Call<DataClass>

    @GET("carrots/get-action/?format=json")
    fun getAllPostsAction() : Call<ActionDataClass>
}