package com.example.musicplayer.viewModel

import android.util.Log
import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import com.example.musicplayer.models.PostModel
import com.example.musicplayer.repository.PostRepository
import com.example.musicplayer.requests.ApiRequest
import com.example.musicplayer.requests.RequestHelper

class MainViewModel: ViewModel() {
    private val request: ApiRequest = RequestHelper().getInstance()
    lateinit var liveData: MutableLiveData<List<PostModel>>
    val repository = PostRepository(request)

    fun sendRequest(){
        repository.fetchAllPosts()
    }
    fun getPosts(): MutableLiveData<List<PostModel>>{
        return repository.getResult()
    }
}