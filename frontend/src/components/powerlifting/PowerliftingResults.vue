<template>
  <br>
  <h2>Your Results!</h2>

  <b-container>
    <b-row>
      <b-col cols=1></b-col>
      <b-col cols=10 class="powerliftingResultsCol">
        <div class="w-100 p-3">
          <PowerliftingChart
            :chartData="squatChart"
            :highlight="this.liftData.data.squat.highlight"
          />
        </div>
        <p>
          Your squat is in the {{this.formatPercentile(liftData.data.squat.percentile)}} percentile
           for your weight class out of {{liftData.data.squat.count}} competing lifters
        </p>

        <hr>

        <div class="w-100 p-3">
          <PowerliftingChart
            :chartData="benchChart"
            :highlight="this.liftData.data.bench.highlight"
          />
        </div>
        <p>
          Your bench is in the {{this.formatPercentile(liftData.data.bench.percentile)}} percentile
           for your weight class out of {{liftData.data.bench.count}} competing lifters
        </p>

        <hr>

        <div class="w-100 p-3">
          <PowerliftingChart
            :chartData="deadliftChart"
            :highlight="this.liftData.data.deadlift.highlight"
          />
        </div>
        <p>
          Your deadlift is in the {{this.formatPercentile(liftData.data.deadlift.percentile)}} percentile
           for your weight class out of {{liftData.data.deadlift.count}} competing lifters
        </p>
      </b-col>
      <b-col cols=1></b-col>
    </b-row>
  </b-container>
</template>

<style>
  .powerliftingResultsCol {
    background-color: white;
    padding: 20px;
    border-radius: 20px;
  }
</style>

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
  methods: {
    formatPercentile(percentile) {
      let suffix = '';
      switch (percentile % 10) {
        case 0:
          suffix = 'th';
          break;
        case 1:
          suffix = 'st';
          break;
        case 2:
          suffix = 'nd';
          break;
        case 3:
          suffix = 'rd';
          break;
        case 4:
        case 5:
        case 6:
        case 8:
        case 9:
          suffix = 'th';
          break;
        default:
          suffix = '';
      }
      return percentile + suffix;
    },
  },
};
</script>
