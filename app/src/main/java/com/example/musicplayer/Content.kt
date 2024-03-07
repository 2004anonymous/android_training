package com.example.musicplayer

import android.annotation.SuppressLint
import android.media.MediaPlayer
import android.net.Uri
import android.os.Bundle
import android.view.GestureDetector
import android.view.MotionEvent
import android.view.View
import android.view.View.OnTouchListener
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.example.musicplayer.databinding.ActivityContentBinding

class Content : AppCompatActivity(){

    private lateinit var bind: ActivityContentBinding
    var isPlaying = false
    private val videoUrl = "https://player.vimeo.com/external/447672569.sd.mp4?s=3afe553437a2b0cf575e154214df2b3f25c35d62&profile_id=164&oauth2_token_id=57447761"

    @SuppressLint("ClickableViewAccessibility")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        bind = ActivityContentBinding.inflate(layoutInflater)
        setContentView(bind.root)

        bind.videoView.setVideoURI(Uri.parse(videoUrl))
        bind.videoView.setOnPreparedListener(MediaPlayer.OnPreparedListener {
            bind.progressLayout.visibility = View.GONE
            it.start()
            isPlaying = true
        })
    }

    override fun onStart() {
        super.onStart()
        bind.progressLayout.visibility = View.VISIBLE
    }
}