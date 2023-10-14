import { PieChart } from "@carbon/charts-react";
import "./_nutriens_pie.scss";
import "@carbon/charts/styles.css";

const NutriensPie = ({ foodSummary }) => {
  console.log(foodSummary);

  const getRusNames = (key) => {
    switch (key) {
      case "protein":
        return "Белки";
      case "fat":
        return "Жиры";
      case "carbohydrate":
        return "Углеводы";
    }
  };

  return (
    <PieChart
      data={Object.keys(foodSummary)
        .filter((k) => k != "calories")
        .map((key) => {
          return { group: getRusNames(key), value: foodSummary[key] };
        })}
      options={{
        title: "Доля БЖУ",
        height: "200px",
        legend: {
          enabled: true,
          alignment: "left",
          position: "left",
        },
        toolbar: {
          enabled: false,
        },
      }}
    ></PieChart>
  );
};

export default NutriensPie;
