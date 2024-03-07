package com.example.musicplayer

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.Observer
import androidx.lifecycle.ViewModelProvider
import com.example.musicplayer.adapters.ContentAdapter
import com.example.musicplayer.databinding.ActivityMainBinding
import com.example.musicplayer.models.ContentModel
import com.example.musicplayer.models.PostModel
import com.example.musicplayer.utilities.Utils
import com.example.musicplayer.viewModel.MainViewModel


class MainActivity : AppCompatActivity(), ContentAdapter.OnContentClickListener {

    private lateinit var bind : ActivityMainBinding
    private lateinit var contentList : ArrayList<ContentModel>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        bind = ActivityMainBinding.inflate(layoutInflater)
        setContentView(bind.root)

        val mainViewModel: MainViewModel = ViewModelProvider(this)[MainViewModel::class.java]
        contentList = ArrayList<ContentModel>()

        mainViewModel.sendRequest()
        mainViewModel.getPosts().observe(this,Observer<List<PostModel>>{
            var count = 0
            contentList.clear()
            while (count < it.size){
                contentList.add(ContentModel(it.get(count).userId,it.get(count).title))
                count += 1
            }

            val adapter: ContentAdapter = ContentAdapter(applicationContext,contentList,this)
            bind.contentRecycler.adapter = adapter
            adapter.notifyDataSetChanged()


        })

    }

    override fun onContentClick() {
        Toast.makeText(this,"Clicked !",Toast.LENGTH_SHORT).show()
    }
}