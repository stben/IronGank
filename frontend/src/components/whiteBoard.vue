<template>
  <div class="board">
    <this.canvas id="this.canvas"
                 class="this.canvas-line this.canvas">浏览器不支持this.canvas</this.canvas>

    <div id="opts"
         class="opts">
      <div class="opts-layer">
        <div class="setting">
          <span id="setColor"
                class="setColor"></span>
          <span id="setLineWidth"
                class="setSize"></span>
          <div class="setColor-layer"
               id="color">
            <ul>
              <li class="color-item col_red"
                  style="background-color: #000"></li>
              <li class="color-item col_red"
                  style="background-color: #fff"></li>
              <li class="color-item col_red"
                  style="background-color: #d1021c"></li>
              <li class="color-item col_red"
                  style="background-color: #fddc01"></li>
              <li class="color-item col_red"
                  style="background-color: #7dd21f"></li>
              <li class="color-item col_red"
                  style="background-color: #228bf8"></li>
              <li class="color-item col_red"
                  style="background-color: #9b0df5"></li>
              <li class="color-item col_red"
                  style="background-color: #7a3e3e"></li>
              <li class="color-item col_red"
                  style="background-color: #f443ab"></li>
              <li class="color-item col_red"
                  style="background-color: #b9fd01"></li>
              <li class="color-item col_red"
                  style="background-color: #1cb114"></li>
              <li class="color-item col_red"
                  style="background-color: #135b88"></li>
              <li class="color-item col_red"
                  style="background-color: #1516bd"></li>
              <li class="color-item col_red"
                  style="background-color: #003300"></li>
              <li class="color-item col_red"
                  style="background-color: #330000"></li>
              <li class="color-item col_red"
                  style="background-color: #336600"></li>
              <li class="color-item col_red"
                  style="background-color: #999966"></li>
              <li class="color-item col_red"
                  style="background-color: #9900FF"></li>
            </ul>
          </div>
          <div class="setSize-layer"
               id="lineWidth">
            <ul>
              <li class="line-item col_size">2</li>
              <li class="line-item col_size">4</li>
              <li class="line-item col_size">6</li>
              <li class="line-item col_size">8</li>
              <li class="line-item col_size">10</li>
              <li class="line-item col_size">12</li>
              <li class="line-item col_size">20</li>
            </ul>
          </div>
        </div>
        <div id="line"
             class="opt line"
             title="画笔"></div>
        <div id="straightLine"
             class="opt straightLine"
             title="直线"></div>
        <div id="rect"
             class="opt rect"
             title="矩形"></div>
        <div id="round"
             class="opt round"
             title="圆形"></div>
        <div id="text"
             class="opt text"
             title="填写文本后，点击绘制"></div>
        <div id="delete"
             class="opt delete"
             title="选中后高亮，点击删除"></div>
        <div id="undo"
             class="opt back"
             title="撤回上一步"></div>
        <div id="clearAll"
             class="opt clear"
             title="清空"></div>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  name: 'whiteBoard',
  created: function () {
  },
  data () {
    return {
      canvas: '',
      context: '',
      cvsW: '',
      cvsH: '',
      container: {
        selected: {
          id: '',
          extensionWidth: 1,
          lineColor: 'red' // '#00ff00'
        },
        session: {}
      }
    }
  },
  methods: {
    Canvas (cvs, ctx) {
      this.canvas = cvs
      this.context = ctx
      this.cvsW = cvs.width
      this.cvsH = cvs.height
    },
    redraw () {
      this.context.clearRect(0, 0, this.canvas.width, this.canvas.height)
      var o, lineColor, lineWidth
      for (var key in this.container.session) {
        o = this.container.session[key]
        lineColor = o.lineColor
        lineWidth = o.lineWidth
        if (this.container.selected.id === o.id) {
          lineColor = this.container.selected.lineColor
          lineWidth = o.lineWidth * 1 + this.container.selected.extensionWidth
        }
        switch (o.type) {
          case 'line': {
            // 线条
            if (o.points.length < 2) break

            this.context.beginPath() // 起始一条路径，或重置当前路径
            this.context.moveTo(o.points[0].x * this.cvsW, o.points[0].y * this.cvsH) // 把路径移动到画布中的指定点，不创建线条
            for (var i = 1, len = o.points.length; i < len; i++) {
              this.context.lineTo(o.points[i].x * this.cvsW, o.points[i].y * this.cvsH) // 添加一个新点，然后在画布中创建从该点到最后指定点的线条
            }
            this.context.strokeStyle = lineColor // 设置或返回用于笔触的颜色、渐变或模式
            this.context.lineWidth = lineWidth // 设置或返回当前的线条宽度
            this.context.stroke() // 绘制已定义的路径
            this.context.closePath() // 创建从当前点回到起始点的路径
            break
          }
          case 'straightLine': {
            // 直线
            this.context.beginPath()
            this.context.moveTo(o.startDot.x * this.cvsW, o.startDot.y * this.cvsH)
            this.context.lineTo(o.endDot.x * this.cvsW, o.endDot.y * this.cvsH)
            this.context.strokeStyle = lineColor
            this.context.lineWidth = lineWidth
            this.context.stroke()
            this.context.closePath()
            break
          }
          case 'rect': {
            // 矩形
            this.context.beginPath()
            this.context.rect(
              o.startDot.x * this.cvsW,
              o.startDot.y * this.cvsH,
              o.endDot.x * this.cvsW - o.startDot.x * this.cvsW,
              o.endDot.y * this.cvsH - o.startDot.y * this.cvsH
            )
            this.context.strokeStyle = lineColor
            this.context.lineWidth = lineWidth
            // this.context.fill();
            this.context.stroke()
            break
          }
          case 'round': {
            // 圆形
            this.context.beginPath()
            this.context.arc(
              o.startDot.x * this.cvsW,
              o.startDot.y * this.cvsH,
              o.r * (this.cvsW / this.cvsH),
              0,
              2 * Math.PI
            )
            this.context.strokeStyle = lineColor
            this.context.lineWidth = lineWidth
            this.context.stroke()
            break
          }
          case 'text': {
            // 文本
            this.context.font = parseInt(lineWidth) * 10 + 'px serif'
            this.context.fillStyle = lineColor
            this.context.fillText(
              o.content,
              o.startDot.x * this.cvsW,
              o.startDot.y * this.cvsH
            )
            break
          }
          default:
            continue
        }
      }
    },
    prototype () {
      let self = this
      drawing: (d) => {
        if (d.type === 'delete') {
          delete self.container.session[d.id]
        } else {
          self.container.session[d.id] = d
        }

        redraw() // 重新绘制画布
      }
      // 清空 画板
      clearAll: (d) => {
        self.canvas.width = self.canvas.width
        self.container.session = {}
      }
      setWH: (w, h) => {
        cvsW = w
        cvsH = h
      }
      getContainer: {
        return self.container
      }
      getLastOptId: {
        let lastTime = 0
        let id = ''
        for (var key in self.container.session) {
          if (lastTime < self.container.session[key].time) {
            lastTime = self.container.session[key].time
            id = self.container.session[key].id
          }
        }
        return id
      },
      redraw: redraw
    },
  }
}
</script>

<script src="../assets/js/UUID.js" charset="utf-8"></script>
<script src="../assets/js/qbian.js" charset="utf-8"></script>
<script src="../assets/js/Canvas.js" charset="utf-8"></script>
<script src="../assets/js/index.js" charset="utf-8"></script>

<style scoped>
@import "../assets/css/whiteBoard.css";
</style>
