<template>
  <p>{{liftData}}</p>
</template>

<script>
// import PowerliftingChart from './PowerliftingChart.vue';

export default {
  props: ['liftData'],
  /* components: {
    PowerliftingChart,
  }, */
  data() {
    console.log(this.liftData);
  },
};
</script>
