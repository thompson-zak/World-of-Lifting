<template>
  <div @click="returnHome" class="navButton">
    <!-- Left arrow icon -->
    <span>&#8592; </span>
    <span> Home Page</span>
  </div>
</template>

<script>
export default {
  name: 'HomeButton',
  methods: {
    returnHome() {
      this.$router.push({ path: '/' });
    },
  },
};
</script>
