<template>
<el-main>
  <object>
    <embed :src="uri" width="100%" height="100%" />
  </object>
</el-main>
</template>

<script>
export default {
  name: 'SwfPlayer',
  props: ['uri']
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
