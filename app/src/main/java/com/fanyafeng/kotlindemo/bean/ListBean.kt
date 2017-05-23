package com.fanyafeng.kotlindemo.bean

import android.os.Parcel
import android.os.Parcelable

/**
 * Author： fanyafeng
 * Data： 17/5/23 下午4:17
 * Email: fanyafeng@live.cn
 */
class ListBean : Parcelable {
    var title: String? = null

    constructor(title: String) {
        this.title = title
    }

    public constructor(`in`: Parcel) {
        title = `in`.readString()
    }

    override fun writeToParcel(dest: Parcel, flags: Int) {
        dest.writeString(title)
    }

    override fun describeContents(): Int {
        return 0
    }

    override fun toString(): String {
        return "ListBean{" +
                "title='" + title + '\'' +
                '}'
    }

    companion object {

        val CREATOR: Parcelable.Creator<ListBean> = object : Parcelable.Creator<ListBean> {
            override fun createFromParcel(`in`: Parcel): ListBean {
                return ListBean(`in`)
            }

            override fun newArray(size: Int): Array<ListBean?> {
                return arrayOfNulls(size)
            }
        }
    }
}
