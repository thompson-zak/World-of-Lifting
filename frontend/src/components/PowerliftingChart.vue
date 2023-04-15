<template>
  <Scatter :data="chartData" :options="chartOptions" />
</template>

<script>
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Scatter } from 'vue-chartjs';
import annotationPlugin from 'chartjs-plugin-annotation';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  annotationPlugin,
);

export default {
  name: 'PowerliftingChart',
  props: ['chartData', 'highlight'],
  components: {
    Scatter,
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        tooltips: {
          intersect: false,
        },
        showLine: true,
        plugins: {
          annotation: {
            annotations: {
              point1: {
                type: 'point',
                xValue: this.highlight.x,
                yValue: this.highlight.y,
                backgroundColor: 'rgba(255, 99, 132, 0.25)',
              },
            },
          },
        },
      },
    };
  },
};
</script>
