<template>
  <mu-paper class="paper">
    <mu-tabs :value.sync="active" color="white" indicator-color="blue" center class="tabs">
      <mu-tab style="color: #9e9e9e" to="/teacher/pickStudent/audit">待审核</mu-tab>
      <mu-tab style="color: #03a9f4">已通过</mu-tab>
    </mu-tabs>
    <div v-if="active===1" class="list">
      <mu-list>
        <mu-list-row v-for="item in acceptedList" :key="item.stuNo">
          <mu-list-item>
            <mu-list-item-title>姓名：{{item.stuName}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;学号：{{item.stuNo}}</mu-list-item-title>
            <mu-button flat color="error" @click="remove($event)">移除</mu-button>
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
  props: ['acceptedList'],
  data() {
    return {
      active: 1
    }
  },
  methods: {
    remove(e) {
      e.currentTarget.style.display = 'none'
      e.currentTarget.nextElementSibling.style.display = 'inline'
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
