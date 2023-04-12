<template>
  <PowerliftingChart :chartData="squatChart" />
  <!-- <PowerliftingChart :chartData="benchData" />
  <PowerliftingChart :chartData="deadliftData" /> -->
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
    const rawSquatData = this.liftData.data.squat;
    const { standardDev, mean } = rawSquatData;

    const squatData = new Array(7);
    for (let i = 1; i <= 3; i += 1) {
      // TODO - These are somehow showing as Nan?
      squatData[3 - i] = mean - standardDev;
      squatData[3 + i] = mean + standardDev;
    }
    squatData[3] = mean;

    const squatChart = {
      labels: squatData,
      datasets: [
        {
          label: 'Squat Performance',
          backgroundColor: '#f87979',
          data: squatData,
        },
      ],
    };

    return {
      squatChart,
    };
  },
};
</script>
