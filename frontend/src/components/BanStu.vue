<template>
  <div id="BanStu">
    <TeacherFrame :selected="'2'" :title="'房间 '+roomNo+'：禁言学生列表'" :roomNo="roomNo"></TeacherFrame>
    <mu-paper class="paper">
      <mu-list class="list">
        <mu-list-row v-for="item in banList" :key="item.stuNo">
          <mu-list-item>
            <mu-list-item-title>姓名：{{item.stuName}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;学号：{{item.stuNo}}</mu-list-item-title>
            <mu-button flat color="error" v-bind:id="item.stuNo" @click="remove($event)">解除</mu-button>
            <span class="removehint">已解除</span>
          </mu-list-item>
          <mu-divider></mu-divider>
        </mu-list-row>
      </mu-list>
    </mu-paper>
  </div>
</template>

<script>
import TeacherFrame from './TeacherFrame'
export default {
  name: 'BanStu',
  components: {
    TeacherFrame
  },
  data() {
    return {
      roomNo: this.$route.params.roomNo,
      banList: [
      ]
    }
  },
  mounted () {
    this.getBanStudents()
  },
  methods: {
    remove(e) {
      let postData = {
        'stuNo': e.currentTarget.id,
        'roomNo': this.roomNo
      }
      let et = e.currentTarget
      this.$axios.post('api/teacher/banStudent',
        this.$Qs.stringify(postData)
      )
        .then((response) => {
          if (response.data.code === '0000') {
            et.style.display = 'none'
            et.nextElementSibling.style.display = 'inline'
          } else alert(response.data.msg)
        })
    },
    getBanStudents() {
      this.$axios.request({
        url: '/api/teacher/banStudent',
        params: {
          'roomNo': this.$route.params.roomNo
        },
        method: 'get'
      }).then((response) => {
        this.banList = response.data.banList
      })
    }
  }
}
</script>

<style scoped>
  .paper{
    margin: -430px 300px;
  }
  .list{
    width: 600px;
    margin: 250px auto;
  }
  .removehint{
    display: none;
    color: #f44336;
    width: 80px;
  }
</style>
