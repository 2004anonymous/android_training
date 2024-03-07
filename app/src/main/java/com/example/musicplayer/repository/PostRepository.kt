package com.example.musicplayer.repository

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import com.example.musicplayer.models.PostModel
import com.example.musicplayer.requests.ApiRequest
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class PostRepository(private var request: ApiRequest) {

    var resultLiveData: MutableLiveData<List<PostModel>> = MutableLiveData()


    fun fetchAllPosts(){
        request.fetchAllPosts().enqueue(object : Callback<List<PostModel>>{
            override fun onResponse(
                call: Call<List<PostModel>>,
                response: Response<List<PostModel>>
            ) {
                resultLiveData.postValue(response.body())
            }

            override fun onFailure(call: Call<List<PostModel>>, t: Throwable) {
                Log.d("error1",t.message.toString())
            }

        })

    }
    fun getResult(): MutableLiveData<List<PostModel>> {
        return resultLiveData;
    }
}