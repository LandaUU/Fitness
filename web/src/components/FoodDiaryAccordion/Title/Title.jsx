const Title = ({ mealName, food }) => {
  let sumOfCalories = 0;
  let sumOfFat = 0;
  let sumOfProtein = 0;
  let sumOfCarbohydrate = 0;
  food.forEach((element) => {
    sumOfCalories += element.calories;
    sumOfFat += element.fat;
    sumOfProtein += element.protein;
    sumOfCarbohydrate += element.carbohydrate;
  });
  return (
    <>
      <div>
        <h3 className="title-meal-name">{mealName}</h3>
        <span className={"food-diary-acc-title-secondary-info"}>
          {sumOfCalories} калорий
        </span>
      </div>
      <hr />
      <div>
        <span className={"food-diary-acc-title-secondary-info"}>
          {sumOfProtein.toFixed(2)} белки
        </span>
        <span className={"food-diary-acc-title-secondary-info"}>
          {sumOfFat.toFixed(2)} жиры
        </span>
        <span className={"food-diary-acc-title-secondary-info"}>
          {sumOfCarbohydrate.toFixed(2)} углеводы
        </span>
      </div>
    </>
  );
};

export default Title;
