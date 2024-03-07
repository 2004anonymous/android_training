package com.example.musicplayer.requests

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

class RequestHelper{
    private val BASE_URl = "https://jsonplaceholder.typicode.com"
    fun getInstance():ApiRequest{
        val retrofit = Retrofit.Builder().baseUrl(BASE_URl).addConverterFactory(
            GsonConverterFactory.create()).build()
        return retrofit.create(ApiRequest::class.java)
    }
}