package com.fanyafeng.kotlindemo.activity

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView

import com.fanyafeng.kotlindemo.R
import com.fanyafeng.kotlindemo.BaseActivity

//需要搭配Baseactivity，这里默认为Baseactivity,并且默认BaseActivity为包名的根目录
class MainActivity : BaseActivity(), View.OnClickListener {
    val a: Int = 1
    var btnShow1: Button? = null
    var tvShow: TextView? = null
    var btnShow2: Button? = null
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        //这里默认使用的是toolbar的左上角标题，如果需要使用的标题为中心的采用下方注释的代码，将此注释掉即可
        title = getString(R.string.title_activity_main)
        isSetNavigationIcon = false

        initView()
        initData()
    }

    override fun onResume() {
        super.onResume()
        //toolbar_center_title.setText(getString(R.string.title_activity_main));
    }

    //初始化UI控件
    private fun initView() {
        btnShow1 = findViewById(R.id.btnShow1) as Button
        btnShow1!!.setOnClickListener(this)
        btnShow2 = findViewById(R.id.btnShow2) as Button
        btnShow2!!.setOnClickListener(this)
        tvShow = findViewById(R.id.tvShow) as TextView
    }

    //初始化数据
    private fun initData() {
//        btnShow1!!.setOnClickListener { tvShow!!.text = "你好" }
    }

    override fun onClick(v: View) {
        when (v) {
            btnShow1 -> {
                tvShow!!.text = "你好"
            }
            btnShow2 -> {
                startActivity(Intent(this, ListActivity::class.java))
            }
        }
    }

    fun sum(a: Int, b: Int): Int {
        return a + b
    }

}
