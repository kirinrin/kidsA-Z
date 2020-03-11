<template>
  <el-container v-if="showType == 'list'">
    <ListView :playlist="playlist.sub" @change-item="changeSubPlaylist"></ListView>
    <MainView :playlist="sublist" :playUri="''"></MainView>
  </el-container>
  <MainView v-else :playlist="playlist.sub" :playUri="''"></MainView>
</template>

<script>
import MainView from "./MainView";
import ListView from "./ListView";
export default {
  name: "MainContainer",
  data: function(){
    return {
      sublist: this.playlist.sub[0].sub
    }
  },
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
      this.sublist = this.playlist.sub[index].sub
    }
  },
  components: { ListView, MainView }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
