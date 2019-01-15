<template>
  <div>
      <teacherIndexFrame :selected="''" :title="'主页 '"></teacherIndexFrame>
      <mu-paper class="paper"  z-depth="4">
        <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="list">
          <template slot-scope="scope">
            <td>{{scope.row.name}}</td>
            <td><mu-button v-bind:id="scope.row.roomId" color="primary" @click="getRoomInfo($event)">编辑</mu-button>
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
      list: []
    }
  },
  mounted: function () {
    this.getTeacherRooms()
  },
  methods: {
    handleSortChange ({name, order}) {
      this.list = this.list.sort((a, b) => order === 'asc' ? a[name] - b[name] : b[name] - a[name])
    },
    getRoomInfo(e) {
      this.$router.push({ name: 'RoomManage', params: {roomNo: e.currentTarget.id} })
    },
    getTeacherRooms: function() {
      this.$axios.get('/api/teacher/teacherIndex')
        .then((response) => {
          this.list = response.data.roomList
        })
    },
    live() {}
  }
}
</script>
<style scoped>
.paper{
    margin: 50px auto;
    width: 850px;
  }
</style>
