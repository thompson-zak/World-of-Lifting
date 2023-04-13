<template>
  <div class="w-100 p-3">
    <PowerliftingChart :chartData="squatChart" />
    <!-- <PowerliftingChart :chartData="benchData" />
    <PowerliftingChart :chartData="deadliftData" /> -->
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
    // Create all objects for squat chart
    const squatCoordinates = this.liftData.data.squat.coordinates;

    const squatChart = {
      datasets: [
        {
          label: 'Squat Performance',
          backgroundColor: '#f87979',
          data: squatCoordinates,
        },
      ],
    };

    return {
      squatChart,
    };
  },
};
</script>
