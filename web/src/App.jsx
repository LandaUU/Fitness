import { createBrowserRouter } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import "./App.scss";
import DatePickerPage from "./content/DatePickerPage";

function groupByMealName(foodData) {
  // Создаем пустой словарь.
  const groupedFoodData = {};

  // Проходим по всем элементам массива foodData.
  for (const food of foodData) {
    // Получаем значение meal_name для текущего элемента.
    const mealName = food.meal_name;

    // Если значение meal_name еще не существует в словаре, создаем новое значение.
    if (!groupedFoodData[mealName]) {
      groupedFoodData[mealName] = [];
    }

    // Добавляем текущий элемент в список для этого значения meal_name.
    groupedFoodData[mealName].push(food);
  }

  // Возвращаем словарь.
  return groupedFoodData;
}

const App = createBrowserRouter([
  {
    path: "/",
    element: <div>Корень!</div>,
  },
  {
    path: "/date_picker",
    element: <DatePickerPage />,
  },
  {
    path: "/dashboard",
    element: <Dashboard />,
    loader: async () => {
      let food_data = [
        {
          id: 5,
          user_id: 1,
          food_name: "Russian 5% Cottage Cheese",
          meal_name: "Breakfast",
          food_category_name: null,
          diary_date: "2023-10-02",
          amount: 1000,
          metric_type: "g",
          calories: 1212,
          protein: 160.01,
          fat: 50.1,
          carbohydrate: 30.16,
        },
        {
          id: 6,
          user_id: 1,
          food_name: "Pea Soup",
          meal_name: "Lunch",
          food_category_name: null,
          diary_date: "2023-10-02",
          amount: 1250,
          metric_type: "g",
          calories: 825,
          protein: 43,
          fat: 14.62,
          carbohydrate: 132.5,
        },
        {
          id: 7,
          user_id: 1,
          food_name: "Mashed Potato",
          meal_name: "Dinner",
          food_category_name: null,
          diary_date: "2023-10-02",
          amount: 500,
          metric_type: "g",
          calories: 500,
          protein: 9,
          fat: 17.7,
          carbohydrate: 78.6,
        },
        {
          id: 8,
          user_id: 1,
          food_name: "Russian Sausage Cutlet",
          meal_name: "Dinner",
          food_category_name: null,
          diary_date: "2023-10-02",
          amount: 285,
          metric_type: "g",
          calories: 698,
          protein: 43.55,
          fat: 40.03,
          carbohydrate: 38.14,
        },
        {
          id: 9,
          user_id: 2,
          food_name: "Флэт Уайт",
          meal_name: "Breakfast",
          food_category_name: null,
          diary_date: "2023-10-04",
          amount: 400,
          metric_type: "g",
          calories: 210,
          protein: 9.76,
          fat: 11.84,
          carbohydrate: 16,
        },
        {
          id: 10,
          user_id: 2,
          food_name: "Сэндвич с Курицей",
          meal_name: "Breakfast",
          food_category_name: null,
          diary_date: "2023-10-04",
          amount: 150,
          metric_type: "g",
          calories: 403,
          protein: 12.9,
          fat: 26.25,
          carbohydrate: 27.6,
        },
        {
          id: 11,
          user_id: 2,
          food_name: "Сырники с Ягодным Джемом",
          meal_name: "Lunch",
          food_category_name: null,
          diary_date: "2023-10-04",
          amount: 200,
          metric_type: "g",
          calories: 393,
          protein: 24,
          fat: 17,
          carbohydrate: 36,
        },
        {
          id: 12,
          user_id: 2,
          food_name: "Суши Сэндвич с Лососем и Суши Сэндвич с Чуккой",
          meal_name: "Lunch",
          food_category_name: null,
          diary_date: "2023-10-04",
          amount: 167,
          metric_type: "g",
          calories: 335,
          protein: 10.19,
          fat: 5.84,
          carbohydrate: 60.45,
        },
        {
          id: 13,
          user_id: 2,
          food_name: "Банан",
          meal_name: "Dinner",
          food_category_name: null,
          diary_date: "2023-10-04",
          amount: 65,
          metric_type: "g",
          calories: 58,
          protein: 0.98,
          fat: 0.06,
          carbohydrate: 14.17,
        },
        {
          id: 14,
          user_id: 2,
          food_name: "Яблоко Сезонное",
          meal_name: "Dinner",
          food_category_name: null,
          diary_date: "2023-10-04",
          amount: 35,
          metric_type: "g",
          calories: 16,
          protein: 0.14,
          fat: 0.14,
          carbohydrate: 3.43,
        },
        {
          id: 15,
          user_id: 2,
          food_name: "Курица Копченая",
          meal_name: "Dinner",
          food_category_name: null,
          diary_date: "2023-10-04",
          amount: 120,
          metric_type: "g",
          calories: 240,
          protein: 19.68,
          fat: 15.6,
          carbohydrate: 0,
        },
        {
          id: 16,
          user_id: 2,
          food_name: "Mashed Potato",
          meal_name: "Dinner",
          food_category_name: null,
          diary_date: "2023-10-04",
          amount: 120,
          metric_type: "g",
          calories: 120,
          protein: 2.16,
          fat: 4.25,
          carbohydrate: 18.86,
        },
      ];

      let result = { food: groupByMealName(food_data) };
      let calories = 0;
      let fat = 0;
      let carbohydrate = 0;
      let protein = 0;
      food_data.forEach((food) => {
        calories += food.calories;
        fat += food.fat;
        carbohydrate += food.carbohydrate;
        protein += food.protein;
      });

      result.food.summary = {
        calories: calories,
        fat: fat,
        carbohydrate: carbohydrate,
        protein: protein,
      };

      result.weight = 100.1;
      result.steps = 15000;

      return result;
    },
  },
]);

export default App;
