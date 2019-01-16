<template>
  <div id="timeTable">
    <TeacherFrame :selected="'4'" :title="'房间 '+roomNo+'：直播间日历'" :roomNo="roomNo"></TeacherFrame>
    <mu-button color="primary" @click="showAlert">新建</mu-button>
    <mu-alert color="primary" @delete="isAlert = false" delete v-if="isAlert" transition="mu-scale-transition" class="alert">
      <mu-paper>
        <mu-form :model="validateForm">
          <mu-form-item>
            <mu-text-field v-model="validateForm.week" prop="week" placeholder="第几周"></mu-text-field>
          </mu-form-item>
          <mu-form-item>
            <mu-text-field v-model="validateForm.weekday" prop="weekday" placeholder="星期几"></mu-text-field>
          </mu-form-item>
          <mu-form-item>
            <mu-text-field v-model="validateForm.begin" prop="begin" placeholder="开始时间"></mu-text-field>
          </mu-form-item>
          <mu-form-item>
            <mu-text-field v-model="validateForm.end" prop="end" placeholder="结束时间"></mu-text-field>
          </mu-form-item>
          <mu-form-item>
            <mu-text-field v-model="validateForm.description" prop="description" placeholder="描述"></mu-text-field>
          </mu-form-item>
          <mu-form-item>
            <mu-button color="success" @click="createTimeInfo">新建</mu-button>
          </mu-form-item>
        </mu-form>
      </mu-paper>
    </mu-alert>
    <mu-expansion-panel v-for="item in timeTableList" :key="item.timeNo">
      <div slot="header">{{item.week}}&nbsp;&nbsp;&nbsp;{{item.weekday}}&nbsp;&nbsp;&nbsp;{{item.begin}}-{{item.end}}：{{item.description}}</div>
      <mu-form >
        <mu-form-item>
          <mu-text-field v-model="item.week" prop="week" placeholder="第几周"></mu-text-field>
        </mu-form-item>
        <mu-form-item>
          <mu-text-field v-model="item.weekday" prop="weekday" placeholder="星期几"></mu-text-field>
        </mu-form-item>
        <mu-form-item>
          <mu-text-field v-model="item.begin" prop="begin" placeholder="开始时间"></mu-text-field>
        </mu-form-item>
        <mu-form-item>
          <mu-text-field v-model="item.end" prop="end" placeholder="结束时间"></mu-text-field>
        </mu-form-item>
        <mu-form-item>
          <mu-text-field v-model="item.description" prop="description" placeholder="描述"></mu-text-field>
        </mu-form-item>
        <mu-form-item>
          <mu-button color="warning"  v-bind:id="item.timeNo" @click="postTimeInfo">修改</mu-button>
        </mu-form-item>
      </mu-form>
    </mu-expansion-panel>
  </div>
</template>

<script>
import TeacherFrame from './TeacherFrame'
export default {
  name: 'timeTable',
  components: {
    TeacherFrame
  },
  data() {
    return {
      roomNo: this.$route.params.roomNo,
      isAlert: false,
      timeTableList: [],
      validateForm: {
        'roomNo': this.$route.params.roomNo,
        'week': '',
        'weekday': '',
        'begin': '',
        'end': '',
        'description': ''
      }
    }
  },
  mounted() {
    this.getRoomTime()
  },
  methods: {
    showAlert() {
      this.isAlert = !this.isAlert
    },
    getRoomTime() {
      let postData = {
        'roomNo': this.$route.params.roomNo
      }
      this.$axios.post('api/teacher/timeTable',
        this.$Qs.stringify(postData)
      ).then((response) => {
        this.timeTableList = response.data.timeTableList
      })
    },
    postTimeInfo(e) {
      let postdata = this.timeTableList[e.currentTarget.id - 1]
      this.$axios.post('api/teacher/modifyTimeTable',
        this.$Qs.stringify(postdata)
      ).then((response) => {
        alert(response.data.msg)
      })
    },
    createTimeInfo() {
      this.$axios.post('api/teacher/newTimeTable',
        this.$Qs.stringify(this.validateForm)
      ).then((response) => {
        alert(response.data.msg)
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
  .alert{
    width: 500px;
    height: 400px;
  }
</style>
