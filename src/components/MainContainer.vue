<template>
  <el-container v-if="showType == 'list'">
    <ListView :playlist="playlist.sub" @chnage-item="changeSubPlaylist"></ListView>
    <MainView :playlist="playlist.sub[0].sub"></MainView>
  </el-container>
  <MainView v-else :playlist="playlist.sub"></MainView>
</template>

<script>
import MainView from "./MainView";
import ListView from "./ListView";
export default {
  name: "MainContainer",
  props: ["playlist"],
  computed: {
    showType: function() {
      var data = this.playlist;
      if (data.sub != undefined && data.sub[0].sub != undefined) {
        return "list";
      } else if (data.sub != undefined) {
        return "collection";
      } else {
        console.log("Error with calc show type");
        return "ERROR";
      }
    }
  },
  methods: {
    changeSubPlaylist: function(index) {
      console.log("click sub menu " + index);
      // this.subPlaylist = this.playlist.sub[index].sub
    }
  },
  components: { ListView, MainView }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
