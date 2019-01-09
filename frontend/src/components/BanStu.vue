<template>
  <div id="BanStu">
    <TeacherFrame :selected="'2'" :title="'房间 '+roomNo+'：禁言学生列表'"></TeacherFrame>
    <mu-paper class="paper">
      <mu-list class="list">
        <mu-list-row v-for="item in banList">
          <mu-list-item>
            <mu-list-item-title>姓名：{{item.stuName}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;学号：{{item.stuNo}}</mu-list-item-title>
            <mu-button flat color="error" @click="remove($event)">解除</mu-button>
            <span class="removehint">已解除</span>
          </mu-list-item>
          <mu-divider></mu-divider>
        </mu-list-row>
      </mu-list>
    </mu-paper>
  </div>
</template>

<script>
import TeacherFrame from './TeacherFrame'
export default {
  name: 'BanStu',
  components: {
    TeacherFrame
  },
  data() {
    return {
      roomNo: 30150, // 要把房间号改了
      banList: [
        {stuName: '张三', stuNo: '20162358'}, {stuName: '李四', stuNo: '20162362'}, {stuName: '王五',stuNo: '20162351'}
      ]
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
    margin: -430px 300px;
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
