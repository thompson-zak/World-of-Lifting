<template>
  <b-navbar type="dark" variant="light">
        <b-navbar-brand href="#">World of Lifting</b-navbar-brand>
  </b-navbar>
  <PowerliftingForm @analyzeLiftsData="onFormSubmit"/>
  <PowerliftingChart
    loaded='{{this.loaded}}'
    chartData='{{this.chartData}}'
    chartOptions='{{this.chartOptions}}' />
</template>

<script>
import PowerliftingForm from './PowerliftingForm.vue';
import PowerliftingChart from './PowerliftingChart.vue';

export default {
  components: {
    PowerliftingForm,
    PowerliftingChart,
  },
  methods: {
    onFormSubmit(data) {
      // This is where you will update everything with emitted data
      console.log(data);
    },
  },
  data() {
    return {
      loaded: false,
      chartData: null,
      chartOptions: null,
    };
  },
};
</script>
