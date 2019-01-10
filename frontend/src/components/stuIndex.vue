<template>
    <div>
        <stuFrame :selected="''" :title="'学生 '+stuNo+''"></stuFrame>
        <mu-paper class="paperstu"  z-depth="4">
            <mu-form :model="form" class="mu-demo-form" :label-position="labelPosition" label-width="100">
                <mu-form-item prop="select" label="授课老师">
                    <mu-select v-model="form.select">
                        <mu-option v-for="option,index in options" :key="option" :label="option" :value="option"></mu-option>
                    </mu-select>
                 </mu-form-item>
            </mu-form>
            <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="list">
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
      list: [
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
        }
      ]
    }
  },
  methods: {
    handleSortChange ({name, order}) {
      this.list = this.list.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name])
    },
    f () {
      this.$router.push('teachingRoom')
    }
  }
}
</script>

<style scoped>
.paperstu{
    margin: 100px 270px;
  }
</style>
