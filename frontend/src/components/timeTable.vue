<template>
  <div id="timeTable">
    <teacherFrame :selected="'4'" :title="'房间 '+roomNo+'：直播间日历'" :roomNo="roomNo"></teacherFrame>
    <mu-button color="success" @click="showAlert" class="button1">新建</mu-button>
    <mu-alert @delete="isAlert = false" delete v-if="isAlert" transition="mu-scale-transition" color="white" class="alert">
      <mu-paper :z-depth="2" class="paper">
        <mu-form :model="validateForm" class="form1">
          第&nbsp;
          <mu-select v-model="validateForm.week" ref="week" class="select">
            <mu-option v-for="option in weekoptions" :key="option" :label="option" :value="option"></mu-option>
          </mu-select>
          &nbsp;周：星期&nbsp;
          <mu-select v-model="validateForm.weekday" ref="weekday" class="select">
            <mu-option v-for="option in weekdayoptions" :key="option" :label="option" :value="option"></mu-option>
          </mu-select>
          <mu-text-field v-model="validateForm.begin" prop="begin" placeholder="开始时间" class="begin"></mu-text-field>
          -
          <mu-text-field v-model="validateForm.end" prop="end" placeholder="结束时间" class="end"></mu-text-field>
          <mu-text-field v-model="validateForm.description" prop="description" label="描述" class="description"></mu-text-field>
          <mu-row>
            <mu-button color="primary" @click="createTimeInfo" class="button2" flat>创建</mu-button>
          </mu-row>
        </mu-form>
      </mu-paper>
    </mu-alert>
    <mu-expansion-panel v-for="item in timeTableList" :key="item.timeNo" class="list">
      <div slot="header" class="text">第{{item.week}}周：星期{{item.weekday}}&nbsp;&nbsp;&nbsp;{{item.begin}}-{{item.end}}：{{item.description}}</div>
      <mu-form class="form2">
        第&nbsp;
        <mu-select v-model="item.week" ref="week" class="select">
          <mu-option v-for="option in weekoptions" :key="option" :label="option" :value="option"></mu-option>
        </mu-select>
        &nbsp;周：星期&nbsp;
        <mu-select v-model="item.weekday" ref="weekday" class="select">
          <mu-option v-for="option in weekdayoptions" :key="option" :label="option" :value="option"></mu-option>
        </mu-select>
        <mu-text-field v-model="item.begin" prop="begin" placeholder="开始时间" class="begin"></mu-text-field>
        -
        <mu-text-field v-model="item.end" prop="end" placeholder="结束时间" class="end"></mu-text-field>
        <mu-text-field v-model="item.description" prop="description" label="描述" class="description"></mu-text-field>
        <mu-button color="primary" v-bind:id="item.timeNo" @click="postTimeInfo" class="button3" flat>确认修改</mu-button>
      </mu-form>
    </mu-expansion-panel>
  </div>
</template>

<script>
import teacherFrame from './teacherFrame'
export default {
  name: 'timeTable',
  components: {
    teacherFrame
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
      },
      weekoptions: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
      weekdayoptions: [1, 2, 3, 4, 5, 6, 7]
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
  .form1{
    margin-top: 20px;
    margin-left: 0px;
    width: 750px;
  }
  .form2{
    margin: 0 auto;
  }
  .list{
    margin: 0 auto;
    width: 750px;
  }
  .button1{
    margin-top: 30px;
    margin-left: -950px;
  }
  .button2{
    margin-top: 0px;
    margin-left: 300px;
  }
  .alert{
    margin-left: 390px;
    margin-top: -20px;
    margin-bottom: 50px;
    width: 700px;
    height: 200px;
  }
  .paper{
    margin-left: -20px;
    margin-top: 0;
    width: 750px;
    height: 230px;
  }
  .text{
    font-size: 13px;
  }
  .select{
    width: 80px;
  }
  .begin{
    margin-left: 50px;
    width: 150px;
  }
  .end{
    margin-left: 5px;
    width: 150px;
  }
  .description{
    width: 670px;
  }
  .button3{
    margin-left: -50px;
  }
</style>
