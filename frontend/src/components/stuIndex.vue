<template>
    <div>
        <stuFrame :selected="''" :title="'学生'"></stuFrame>
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
                    <td>{{scope.row.name}}</td>
                    <td>{{scope.row.description}}</td>
                    <td>{{scope.row.departmentName}}</td>
                    <td><mu-button v-bind:id="scope.row.roomNo" color="primary" @click="enterRoom">
                        加入房间
                    </mu-button></td>
                    <td> <mu-button v-bind:id="scope.row.roomNo" color="primary" @click="live">
                        观看
                    </mu-button></td>
                </template>
            </mu-data-table>
        </mu-paper>
    </div>
</template>

<script>
import stuFrame from '../components/stuFrame'
export default {
  name: 'stuIndex',
  components: {
    stuFrame
  },
  data () {
    return {
      options: [
        '软件工程', '计算机', '通信', ' '
      ],
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
    live () {
      this.$router.push('teachingRoom')
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
      if (this.form.select === ' ') this.showList = this.list
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
