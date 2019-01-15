<template>
  <mu-paper class="paper">
    <mu-tabs :value.sync="active" color="white" indicator-color="blue" center class="tabs">
      <mu-tab style="color: #9e9e9e" :to="{ name: 'PickStuAudit', params: {roomNo: roomNo}}">待审核</mu-tab>
      <mu-tab style="color: #03a9f4">已通过</mu-tab>
    </mu-tabs>
    <div v-if="active===1" class="list">
      <mu-list>
        <mu-list-row v-for="item in acceptedList" :key="item.stuNo">
          <mu-list-item>
            <mu-list-item-title>姓名：{{item.stuName}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;学号：{{item.stuNo}}</mu-list-item-title>
            <mu-button flat color="error" v-bind:id="item.stuNo" @click="remove($event)">移除</mu-button>
            <span class="removehint">已移除</span>
          </mu-list-item>
          <mu-divider></mu-divider>
        </mu-list-row>
      </mu-list>
    </div>
  </mu-paper>
</template>

<script>
export default {
  name: 'PickStuTabsAccepted',
  props: ['acceptedList', 'roomNo'],
  data() {
    return {
      active: 1
    }
  },
  methods: {
    remove(e) {
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
            ec.nextElementSibling.style.display = 'inline'
          } else alert(response.data.msg)
        })
    }
  }
}
</script>

<style scoped>
  .paper{
    margin: -50px 300px;
  }
  .tabs{
    margin: -240px auto;
    width: 600px;
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
