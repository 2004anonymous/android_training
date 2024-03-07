package com.example.musicplayer.utilities

import android.content.Context
import android.widget.Toast

class Utils {

    fun showToast(context: Context, msg: String?){
        Toast.makeText(context,msg,Toast.LENGTH_SHORT).show()
    }
}