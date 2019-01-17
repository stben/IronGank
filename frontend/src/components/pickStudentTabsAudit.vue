<template>
  <div id="pickStudentTabsAudit">
    <mu-tabs :value.sync="active" inverse color="blue" indicator-color="blue" center class="tabs">
      <mu-tab>待审核</mu-tab>
      <mu-tab :to="{ name: 'pickStudentAccepted', params: {roomNo: roomNo}}">已通过</mu-tab>
    </mu-tabs>
    <mu-paper :z-depth="2" v-if="active===0" class="paper">
        <mu-data-table :columns="columns" :data="auditList">
          <template slot-scope="item">
            <td>{{item.row.stuNo}}</td>
            <td>{{item.row.stuName}}</td>
            <td>
              <mu-button flat color="success" v-bind:id="item.row.stuNo" @click="agree($event)">通过</mu-button>
              <mu-button flat color="error" v-bind:id="item.row.stuNo" @click="disagree($event)">拒绝</mu-button>
              <span class="agreehint">已通过</span>
              <span class="disagreehint">未通过</span>
            </td>
          </template>
        </mu-data-table>
    </mu-paper>
  </div>
</template>

<script>
export default {
  name: 'pickStudentTabsAudit',
  props: ['auditList', 'roomNo'],
  data() {
    return {
      active: 0,
      columns: [
        { title: '学号', name: 'stuNo' }, { title: '姓名', name: 'stuName' }, { title: '操作', name: '', align: 'center' }
      ]
    }
  },
  methods: {
    agree(e) {
      let postData = {
        'roomNo': this.roomNo,
        'stuNo': e.currentTarget.id,
        'isAccepted': '1'
      }
      let ec = e.currentTarget
      this.$axios.post('api/teacher/pickStudent',
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
        'stuNo': e.currentTarget.id,
        'isAccepted': '0'
      }
      let ec = e.currentTarget
      this.$axios.post('api/teacher/pickStudent',
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
    margin: 100px auto;
    width: 300px;
  }
  .paper{
       margin: -80px auto;
       width: 750px;
     }
  .agreehint{
    display: none;
    color: #4caf50;
    width: 80px;
    margin: 0 80px;
  }
  .disagreehint{
    display: none;
    color: #f44336;
    width: 80px;
    margin: 0 80px;
  }
</style>
