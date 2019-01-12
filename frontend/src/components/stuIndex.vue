<template>
    <div>
        <stuFrame :selected="''" :title="'学生 '+stuNo+''"></stuFrame>
        <mu-paper class="paperstu"  z-depth="4">
            <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                <mu-form-item prop="select" label="授课老师">
                    <mu-select v-model="form.select" @change="onSelected">
                        <mu-option v-for="option,index in options" :key="option" :label="option" :value="option"></mu-option>
                    </mu-select>
                 </mu-form-item>
            </mu-form>
            <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" v-bind:data="showlist">
                <template slot-scope="scope">
                    <td>{{scope.row.name}}</td>
                    <td>{{scope.row.time}}</td>
                <td>{{scope.row.teacher}}</td>
                    <td class="is-right"><mu-button color="primary" @click="f">加入</mu-button></td>
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
        '老王', '老李', '老朱', '老菜',
        '老胡'
      ],
      form: {
        select: ''
      },
      shift: 'movies',
      sort: {
        name: '',
        order: 'asc'
      },
      columns: [
        { title: '课程名称', width: 200, name: 'name' },
        { title: '上课时间', width: 200, name: 'time' },
        { title: '教师', width: 200, name: '' },
        { title: '操作', do: '编辑', width: 200, align: 'center', sortable: true }
      ],
      list: [ // 保存所有数据的总列表
        {
          name: '课程名',
          time: '10:00-11:00',
          teacher: '老王'
        },
        {
          name: '课程名',
          time: '9:00-10:00',
          teacher: '老王'
        },
        {
          name: '课程名',
          time: '13:00-14:00',
          teacher: '老王'
        },
        {
          name: '课程名',
          time: '15:00-16:00',
          teacher: '老王'
        },
        {
          name: '课程名',
          time: '9:00-10:00',
          teacher: '老朱'
        }
      ],
      showlist: [] // 需要展示出来的列表
    }
  },
  methods: {
    handleSortChange ({name, order}) {
      this.list = this.list.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name])
    },
    f () {
      this.$router.push('teachingRoom')
    },
    onSelected () { // 选择框改变时触发的函数
      this.showlist.splice(0, this.showlist.length)
      if (this.form.select === ' ') this.showlist = this.list
      else {
        for (var i = 0; i < this.list.length; i++) {
          if (this.list[i].teacher === this.form.select) {
            this.showlist.push(this.list[i])
          }
        }
      }
    }
  },
  mounted () { // 初始化展示的列表
    for (var i = 0; i < this.list.length; i++) {
      this.showlist.push(this.list[i])
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
