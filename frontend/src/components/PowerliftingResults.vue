<template>
  <div class="w-100 p-3">
    <PowerliftingChart :chartData="squatChart" />
  </div>
  <div class="w-100 p-3">
    <PowerliftingChart :chartData="benchChart" />
  </div>
  <div class="w-100 p-3">
    <PowerliftingChart :chartData="deadliftChart" />
  </div>
</template>

<script>
import PowerliftingChart from './PowerliftingChart.vue';

export default {
  name: 'PowerliftingResults',
  props: ['liftData'],
  components: {
    PowerliftingChart,
  },
  data() {
    // Create all objects for SBD charts
    const squatChart = {
      datasets: [
        {
          label: 'Squat Performance',
          backgroundColor: '#f87979',
          data: this.liftData.data.squat.coordinates,
        },
      ],
    };

    const benchChart = {
      datasets: [
        {
          label: 'Bench Performance',
          backgroundColor: '#63c45e',
          data: this.liftData.data.bench.coordinates,
        },
      ],
    };

    const deadliftChart = {
      datasets: [
        {
          label: 'Deadlift Performance',
          backgroundColor: '#152bd1',
          data: this.liftData.data.deadlift.coordinates,
        },
      ],
    };

    return {
      squatChart,
      benchChart,
      deadliftChart,
    };
  },
};
</script>
