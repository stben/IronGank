<template>
  <div id="banStudent">
    <teacherFrame :selected="'2'" :title="'房间 '+roomNo+'：禁言学生列表'" :roomNo="roomNo"></teacherFrame>
    <mu-paper :z-depth="2" class="paper">
      <mu-data-table :columns="columns" :data="banList">
        <template slot-scope="item">
          <td>{{item.row.stuNo}}</td>
          <td>{{item.row.stuName}}</td>
          <td>
            <mu-button flat color="error" v-bind:id="item.row.stuNo" class="removebutton" @click="remove($event)">解除禁言</mu-button>
            <span class="removehint">已解除</span>
          </td>
        </template>
      </mu-data-table>
    </mu-paper>
  </div>
</template>

<script>
import teacherFrame from './teacherFrame'
export default {
  name: 'banStudent',
  components: {
    teacherFrame
  },
  data() {
    return {
      roomNo: this.$route.params.roomNo,
      banList: [
      ],
      columns: [
        { title: '学号', name: 'stuNo' }, { title: '姓名', name: 'stuName' }, { title: '操作', name: '', align: 'center' }
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
    margin: 120px auto;
    width: 770px;
  }
  .removebutton{
    margin: 0 60px;
  }
  .removehint{
    display: none;
    color: #f44336;
    width: 80px;
    margin: 0 80px;
  }
</style>
