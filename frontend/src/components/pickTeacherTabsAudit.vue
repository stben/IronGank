<template>
  <div id="pickTeacherTabsAudit">
    <mu-tabs :value.sync="active" inverse color="blue" indicator-color="blue" center class="tabs">
      <mu-tab>待审核</mu-tab>
      <mu-tab :to="{ name: 'pickTeacherAccepted', params: {roomNo: roomNo}}">已通过</mu-tab>
    </mu-tabs>
    <mu-paper :z-depth="2" v-if="active===0" class="paper">
      <mu-data-table :columns="columns" :data="auditList">
        <template slot-scope="item">
          <td>{{item.row.username}}</td>
          <td>
            <mu-button flat color="success" v-bind:id="item.row.username" @click="agree($event)" class="agree-button">通过</mu-button>
            <mu-button flat color="error" v-bind:id="item.row.username" @click="disagree($event)">拒绝</mu-button>
            <span class="agree-hint">已通过</span>
            <span class="disagree-hint">未通过</span>
          </td>
        </template>
      </mu-data-table>
    </mu-paper>
  </div>
</template>

<script>
export default {
  name: 'pickTeacherTabsAudit',
  props: ['auditList', 'roomNo'],
  data() {
    return {
      active: 0,
      columns: [
        { title: '账号', name: 'username' }, { title: '操作', name: '', align: 'center' }
      ]
    }
  },
  methods: {
    agree(e) {
      let postData = {
        'roomNo': this.roomNo,
        'teacherNo': e.currentTarget.id,
        'isAccepted': '1'
      }
      let ec = e.currentTarget
      this.$axios.post('api/teacher/pickTeacher',
        this.$Qs.stringify(postData)
      )
        .then((response) => {
          if (response.data.code === '0000') {
            ec.style.display = 'none'
            ec.nextElementSibling.style.display = 'none'
            ec.nextElementSibling.nextElementSibling.style.display = 'inline'
          } else alert(response.data.msg)
        })
    },
    disagree(e) {
      let postData = {
        'roomNo': this.roomNo,
        'teacherNo': e.currentTarget.id,
        'isAccepted': '0'
      }
      let ec = e.currentTarget
      this.$axios.post('api/teacher/pickTeacher',
        this.$Qs.stringify(postData)
      )
        .then((response) => {
          if (response.data.code === '0000') {
            ec.style.display = 'none'
            ec.previousElementSibling.style.display = 'none'
            ec.nextElementSibling.nextElementSibling.style.display = 'inline'
          } else alert(response.data.msg)
        })
    }
  }
}
</script>

<style scoped>
  .tabs{
    margin: 100px 680px;
    width: 300px;
  }
  .paper{
    margin: -80px 400px;
    width: 900px;
  }
  .agree-button{
    margin-left: 110px;
  }
  .agree-hint{
    display: none;
    color: #4caf50;
    width: 80px;
    margin: 0 180px;
  }
  .disagree-hint{
    display: none;
    color: #f44336;
    width: 80px;
    margin: 0 180px;
  }
</style>
