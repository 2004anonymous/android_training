package com.example.musicplayer.requests

import com.example.musicplayer.models.PostModel
import retrofit2.Call
import retrofit2.Response
import retrofit2.http.GET


interface ApiRequest {
    @GET("/posts")
    fun fetchAllPosts(): Call<List<PostModel>>
}