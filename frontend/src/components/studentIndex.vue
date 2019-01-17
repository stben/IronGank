<template>
    <div>
        <studentFrame :selected="''" :title="'首页'"></studentFrame>
        <mu-paper class="paperstu"  z-depth="4">
            <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                <mu-form-item prop="select" label="专业院系">
                    <mu-select v-model="form.select" @change="onSelected">
                        <mu-option v-for="option in options" :key="option" :label="option" :value="option"></mu-option>
                    </mu-select>
                 </mu-form-item>
            </mu-form>
            <mu-data-table :columns="columns"  v-bind:data="showList">
                <template slot-scope="scope">
                    <td>{{scope.row.roomName}}</td>
                    <td>{{scope.row.roomDescription}}</td>
                    <td>{{scope.row.departmentName}}</td>
                    <td><mu-button v-bind:id="scope.row.roomNo" color="primary" @click="enterRoom">
                        加入房间
                    </mu-button></td>
                    <td> <mu-button v-bind:id="scope.row.roomNo" color="primary" @click="live">
                        观看
                    </mu-button></td>
                </template>
            </mu-data-table>
            <mu-dialog title="请输入密码" width="600" max-width="80%" :esc-press-close="false" :overlay-close="false" :open.sync="alert">
               <mu-text-field v-model="password" placeholder="请输入房间密码" ref="password"></mu-text-field>
               <mu-button slot="actions" flat color="primary" @click="closeAlertDialog">取消</mu-button>
               <mu-button slot="actions" flat color="primary" @click="passwordConfirm">确定</mu-button>
            </mu-dialog>
        </mu-paper>
    </div>
</template>

<script>
import studentFrame from './studentFrame'
export default {
  name: 'studentIndex',
  components: {
    studentFrame
  },
  data () {
    return {
      indexRoom: '',
      alert: false,
      wrongPassword: false,
      options: [
        '软件工程', '计算机', '通信', '所有课程'
      ],
      password: '',
      form: {
        select: ''
      },
      shift: 'movies',
      columns: [
        { title: '课程名称', width: 180, name: 'name' },
        { title: '描述', width: 200, name: 'time' },
        { title: '院系', width: 180, name: 'department' },
        { title: '申请', width: 120, align: 'center' },
        { title: '直播', width: 120, align: 'center' }
      ],
      list: [],
      showList: [] // 需要展示出来的列表
    }
  },
  mounted() {
    this.getRooms()
  },
  methods: {
    live (e) {
      let roomNo = e.currentTarget.id
      for (let item of this.list) {
        if (item.roomNo + '' === roomNo) {
          if (item.isPassword === true) {
            this.indexRoom = roomNo
            this.alert = true
          } else {
            this.$router.push({ name: '/student/teachingRoom', params: {roomNo: this.indexRoom} })
          }
        }
      }
    },
    passwordConfirm() {
      let roomNo = this.indexRoom
      for (let item of this.list) {
        if (item.roomNo + '' === roomNo) {
          if (this.password === item.password) {
            this.$router.push({ name: '/student/teachingRoom', params: {roomNo: this.indexRoom} })
          } else {
            alert('密码错误')
          }
        }
      }
    },
    closeAlertDialog() {
      this.alert = false
    },
    enterRoom(e) {
      let ec = e.currentTarget
      this.$axios.request({
        url: '/api/student/studentRoom',
        params: {
          'roomNo': ec.id
        },
        method: 'get'
      }).then((response) => {
        alert(response.data.msg)
      })
    },
    getRooms() {
      this.$axios.request({
        url: '/api/student/studentIndex',
        method: 'get'
      }).then((response) => {
        this.list = response.data.allRooms
        this.showList = response.data.allRooms
      })
    },
    onSelected () { // 选择框改变时触发的函数
      this.showList = []
      if (this.form.select === '所有课程') this.showList = this.list
      else {
        for (let i = 0; i < this.list.length; i++) {
          if (this.list[i].departmentName === this.form.select) {
            this.showList.push(this.list[i])
          }
        }
      }
    }
  }
}
</script>

<style scoped>
.paperstu{
    margin: 100px auto;
    width: 800px;
  }
</style>
