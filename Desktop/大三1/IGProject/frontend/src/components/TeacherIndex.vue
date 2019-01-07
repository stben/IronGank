<template>
  <div>
    <mu-container style="max-width: 800px; width:100%;">
      <mu-bottom-nav :value.sync="shift" shift>
        <mu-bottom-nav-item value="movies"  icon="MyRoom"></mu-bottom-nav-item>
        <mu-bottom-nav-item value="music"  icon="NewRoom"></mu-bottom-nav-item>
        <mu-bottom-nav-item value="books"  icon="AllRoom"></mu-bottom-nav-item>
        <mu-bottom-nav-item value="pictures"  icon="Start"></mu-bottom-nav-item>
      </mu-bottom-nav>
      <mu-paper :z-depth="1">
        <mu-data-table :columns="columns" :sort.sync="sort" @sort-change="handleSortChange" :data="list">
          <template slot-scope="scope">
            <td>{{scope.row.name}}</td>
            <td class="is-right"><mu-button color="primary" @click="f">编辑</mu-button></td>
          </template>
        </mu-data-table>
      </mu-paper>
    </mu-container>
  </div>
</template>

<script>
export default {
  data () {
    return {
      shift: 'movies',
      sort: {
        name: '',
        order: 'asc'
      },
      columns: [
        { title: '课程名称', width: 600, name: 'name' },
        { title: '操作', do: '编辑', width: 200, align: 'center', sortable: true }
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
    }
  }
}
</script>
