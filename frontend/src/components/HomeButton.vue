<template>
  <div @click="returnHome" class="homeButton">
    <!-- Left arrow icon -->
    <span>&#8592; </span>
    <span> Home Page</span>
  </div>
</template>

<style>
  .homeButton {
    margin: 10px;
    font-size: 1.5em;
    font-weight: 700;
  }
</style>

<script>
export default {
  name: 'HomeButton',
  methods: {
    returnHome() {
      console.log('This should take you home!');
      // Not ideal because this causes a hard reload
      this.$router.go();
    },
  },
};
</script>
