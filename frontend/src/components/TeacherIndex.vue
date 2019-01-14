<template>
  <div>
      <teacherIndexFrame :selected="''" :title="'房间 '+roomNo+''"></teacherIndexFrame>
      <mu-paper class="paper"  z-depth="4">
        <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="list">
          <template slot-scope="scope">
            <td>{{scope.row.name}}</td>
            <td><mu-button color="primary" @click="f">编辑</mu-button>
              <mu-button color="primary" @click="live">开播</mu-button>
            </td>
          </template>
        </mu-data-table>
      </mu-paper>
  </div>
</template>
<script>
import teacherIndexFrame from '../components/teacherIndexFrame'
export default {
  name: 'TeacherIndex',
  components: {
    teacherIndexFrame
  },
  data () {
    return {
      shift: 'movies',
      sort: {
        name: '',
        order: 'asc'
      },
      columns: [
        { title: '课程名称', width: 600, name: 'name' },
        { title: '操作', do: '编辑', width: 250, align: 'center', sortable: true }
      ],
      list: [
        {
          name: '课程名'
        },
        {
          name: '课程名'
        },
        {
          name: '课程名'
        },
        {
          name: '课程名'
        }
      ]
    }
  },
  methods: {
    handleSortChange ({name, order}) {
      this.list = this.list.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name])
    },
    f () {
      this.$router.push('RoomManage')
    },
    live () {
      this.$router.push('liveRoom')
    }
  }
}
</script>
<style scoped>
.paper{
    margin: 50px auto;
    width: 850px;
  }
</style>
