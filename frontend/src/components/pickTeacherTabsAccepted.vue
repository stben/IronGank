<template>
  <div id="pickTeacherTabsAccepted">
    <mu-tabs :value.sync="active" inverse color="blue" indicator-color="blue" center class="tabs">
      <mu-tab :to="{ name: 'pickTeacherAudit', params: {roomNo: roomNo}}">待审核</mu-tab>
      <mu-tab>已通过</mu-tab>
    </mu-tabs>
    <mu-paper :z-depth="2" v-if="active===1" class="paper">
      <mu-data-table :columns="columns" :data="acceptedList">
        <template slot-scope="item">
          <td>{{item.row.username}}</td>
          <td>
            <mu-button flat color="error" v-bind:id="item.row.username" @click="remove($event)" class="removebutton">移除</mu-button>
            <span class="removehint">已移除</span>
          </td>
        </template>
      </mu-data-table>
    </mu-paper>
  </div>
</template>

<script>
export default {
  name: 'pickTeacherTabsAccepted',
  props: ['acceptedList', 'roomNo'],
  data() {
    return {
      active: 1,
      columns: [
        { title: '账号', name: 'username' }, { title: '操作', name: '', align: 'center' }
      ]
    }
  },
  methods: {
    remove(e) {
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
            ec.nextElementSibling.style.display = 'inline'
          } else alert(response.data.msg)
        })
    }
  }
}
</script>

<style scoped>
  .tabs{
    top: 40px;
    left: 610px;
    width: 300px;
  }
  .paper{
    margin-top: 60px;
    margin-left: 25%;
    width: 900px;
  }
  .removebutton{
    margin: 0 155px;
  }
  .removehint{
    display: none;
    color: #f44336;
    width: 80px;
    margin: 0 180px;
  }
</style>
