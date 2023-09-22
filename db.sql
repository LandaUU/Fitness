CREATE DATABASE FitnessApp;


CREATE TABLE User (
    id bigserial primary key,
    fio varchar not null,
    lastname varchar not null,
    middlename varchar,
    firstname varchar not null,
    height smallint,
    age smallint,
    birthday timestamp,
    gender varchar,
    created_date timestamp,
    pay_date timestamp,
    next_report_date timestamp,
    deleted_date timestamp,
    exit_date timestamp
);

CREATE TABLE User_Measurement (
    id bigserial primary key,
    user_id bigint not null
    constraint measurement_user_id_fk
    references user,
    pass_date timestamp not null,
    weight real,
    steps integer,
    neck real,
    waist real,
    stomach real,
    hips real,
    hip real,
    shin real,
    chest real,
    biceps real
);

CREATE TABLE Meal (
    id bigserial primary key,
    name varchar not null
);

CREATE TABLE Food (
    id bigserial primary key,
    name varchar not null,
    category_id bigint
);

CREATE TABLE Food_Category (
    id bigserial primary key,
    name varchar not null
)

CREATE TABLE Metric_Types (
    id bigserial primary key,
    type varchar not null,
    description varchar
);

CREATE TABLE Food_Diary (
    id bigserial primary key,
    food_id bigint not null
    constraint diary_food_id_fk
    references food,
    user_id bigint not null
    constraint diary_user_id_fk
    references user,
    meal_id bigint not null
    constraint diary_meal_id_fk
    references meal,
    diary_date timestamp,
    amount real,
    metric_type varchar,
    calories real,
    protein real,
    fat real,
    carbohydrate real,
    calcium real,
    cholesterol real,
    fiber real,
    iron real,
    monounsaturated_fat real,
    polyunsaturated_fat real,
    potassium real,
    saturated_fat real,
    sodium real,
    sugar real,
    vitamin_a real,
    vitamin_c real,
    trans_fat real
);