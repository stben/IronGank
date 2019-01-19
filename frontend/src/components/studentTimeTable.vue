<template>
  <div id="timeTable">
    <studentFrame :selected="'4'"
                  :title="'房间 '+roomNo+'：直播间日历'"
                  :roomNo="roomNo"></studentFrame>
    <mu-button color="success"
               :to="{ name: 'teachingRoom', params: { roomNo: this.roomNo }}"
               class="button1">进入房间</mu-button>
    <div class=list>
      <mu-data-table :columns="columns"
                     :data="timeTableList"
                     hideHeader>
        <template slot-scope="item">
          <td>第{{item.row.week}}周：星期{{item.row.weekday}}&nbsp;&nbsp;
            &nbsp;&nbsp;{{item.row.begin}}-
            {{item.row.end}}：{{item.row.description}}</td>
        </template>
      </mu-data-table>
    </div>
  </div>
</template>
<script>
import studentFrame from './studentFrame'
export default {
  name: 'studentTimeTable',
  components: {
    studentFrame
  },
  data () {
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
      weekdayoptions: [1, 2, 3, 4, 5, 6, 7],
      columns: [
        { title: '', name: '' }
      ]
    }
  },
  mounted () {
    this.getRoomTime()
  },
  methods: {
    getRoomTime () {
      let postData = {
        'roomNo': this.$route.params.roomNo
      }
      this.$axios.post('/api/teacher/timeTable',
        this.$Qs.stringify(postData)
      ).then((response) => {
        this.timeTableList = response.data.timeTableList
      })
    }
  }
}
</script>

<style scoped>
.list {
  margin-top: -35px;
  margin-left: 400px;
  width: 750px;
}
.button1 {
  margin-top: 110px;
  margin-left: -750px;
}
</style>
