import { PieChart } from "@carbon/charts-react";
import "./_nutriens_pie.scss";
import "@carbon/charts/styles.css";

const NutriensPie = ({ foodSummary }) => {
  console.log(foodSummary);
  return (
    <PieChart
      data={Object.keys(foodSummary)
        .filter((k) => k != "calories")
        .map((key) => {
          return { group: key, value: foodSummary[key] };
        })}
      options={{
        title: "Pie",
        height: "200px",
        legend: {
          enabled: false,
        },
        toolbar: {
          enabled: false,
        },
        pie: {
          labels: {
            enabled: false,
          },
        },
      }}
    ></PieChart>
  );
};

export default NutriensPie;
