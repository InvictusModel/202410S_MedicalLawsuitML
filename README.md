![[./images/Pasted image 20241218125539.png]]
This is an in-depth analysis of the impact of gender on promotions and salaries within the context of a lawsuit. This is a group work that I took part in. We had conducted a comprehensive study to shed light on the disparities faced by female doctors in the workplace. 


# **Introduction: Gender Discrimination Lawsuit**

This study is focused on understanding the gender discrimination in promotions and salaries within the medical profession. Our team comprises of Liu Jinming, Li Kexin, Wang Jiale, Chen HouHsuan, Xu Shuhan, and Wang Xiaoyi, all dedicated to providing a thorough analysis.

## **Section 1: Promotion**
![[images/Pasted image 20241218125546.png]]![[images/Pasted image 20241218125551.png]]![[images/Pasted image 20241218125557.png]]![[images/Pasted image 20241218125601.png]]

**1.1 Overall Illustration**

Our analysis begins with an overall illustration of how gender affects promotions. We found that men are more likely to be promoted, which we've supported with a logistic model. Men have a higher promotion probability across all age groups, based on rank, experience, and logistic model analysis.

**Graphic Method**

In our graphic method, we've demonstrated that the defendant might argue men are promoted faster due to obtaining their MD earlier. However, our analysis shows that women are more concentrated in assistant professor roles, while men dominate full and associate professor positions, suggesting significant barriers for women in career advancement.

**Logistics Regression**

Moving on to logistics regression, we've proven that men have a higher likelihood of promotion. Our model output, including the ROC curve and confusion matrix, indicates that both gender and experience significantly impact the odds of getting promoted. With other conditions being equal, the probability of promotion for men is 2.39 times that of women.

**1.3 Higher Promotion Probability for Men at the Same Experience Level**

Our logistic model output reveals that the male promotion curve is steeper and higher than the female curve, leading us to conclude that men have a higher promotion probability than women, even with the same years of experience.

## **Section 2: Salary**

![[images/Pasted image 20241218125607.png]]![[images/Pasted image 20241218125614.png]]![[images/Pasted image 20241218125619.png]]![[images/Pasted image 20241218125624.png]]![[images/Pasted image 20241218125629.png]]![[images/Pasted image 20241218125635.png]]![[images/Pasted image 20241218125641.png]]

**2.1 Overall Illustration**

Shifting our focus to salary, we've observed that women's salary distribution is overall lower than men's. Men hold a greater proportion of high-salary extreme values, while women rarely reach the highest salary brackets.

**Ordinal Encoding and Regularization**

To create a more accurate model, we've converted the department variable from nominal to ordinal based on the annual average salary. This adjustment allowed us to include the department variable in our linear regression model, enhancing prediction accuracy.

**Regularization**

Our multiple linear regression after regularization (Elastic Net) shows that salary is significantly positively correlated with gender. This contradicts the original regression, which did not show a significant correlation, highlighting the importance of regularization in our analysis.

**2.3 Gender Influences Department, Which in Turn Influences Salary**

Our graphic method reveals that high-salary departments predominantly employ men, while low-salary departments have a higher proportion of women. This suggests that women have fewer opportunities to enter high-salary departments, resulting in their overall lower salaries.

**Chi-Square and Moderating Variable Model**

We've used the Chi-square test to determine if there is a significant relationship between gender and department. Our findings show that department is positively correlated with gender. We then built a moderating variable model to investigate if department plays a role in the relationship between gender and salary.

**Variable Moderation**

We created a new variable, Gender*adjDept, to indicate whether the interaction between gender and department influences salary. Our moderating variable model shows that department plays a significant role in positively moderating the relationship between salary and gender. In high-salary departments, men are more likely to receive higher salaries.

**Conclusion**
![[images/Pasted image 20241218125649.png]]
In conclusion, our data clearly demonstrates that gender affects both salary and rank. Men are significantly more likely to hold Associate and Full Professor positions, and according to logistic regression, the probability of promotion for men is 2.39 times that of women. Regularized multiple regression shows a significant positive correlation between salary and gender. Furthermore, our moderating variable model indicates that in high-salary departments, men are more likely to earn higher salaries.

This comprehensive analysis provides a clear picture of the gender disparities within the medical profession, highlighting the need for further investigation and potential interventions to address these inequalities.

