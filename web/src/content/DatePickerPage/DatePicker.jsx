import { useEffect, useState } from "react";
import { DatePicker, DatePickerInput } from "@carbon/react";

const DatePickerPage = () => {
  const [date, setDate] = useState(new Date());

  useEffect(() => {
    console.log("get date");
    console.log(date);
  }, [date]);

  return (
    <DatePicker
      className="date-picker-report"
      datePickerType="single"
      value={date}
      onChange={(value) => {
        console.log("onChange");
        console.log(value);
        setDate(value[0]);
      }}
    >
      <DatePickerInput
        className="date-picker-input-report"
        placeholder="ММ/ДД/ГГГГ"
        labelText="Выберите дату для выгрузки отчета"
        size="md"
      />
    </DatePicker>
  );
};

export default DatePickerPage;
