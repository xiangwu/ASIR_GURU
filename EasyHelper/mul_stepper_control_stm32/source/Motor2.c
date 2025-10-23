#include "stm32f10x.h"                  // Device header
#include "Delay.h"
#include "PWM.h"

//PA2���壬PA3����ת̨
void Motor2_Init(void)
{   	
  
    RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);	

    GPIO_InitTypeDef GPIO_InitStructure;    
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_3;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;			
    GPIO_Init(GPIOA,&GPIO_InitStructure);
 
    GPIO_SetBits(GPIOA,GPIO_Pin_3);
    PWM_Init();		
}

//PA1���壬PA0���򣬴��ʹ�
void Motor3_Init(void)
{   	
  
    RCC_APB2PeriphClockCmd(RCC_APB2Periph_GPIOA, ENABLE);	

    GPIO_InitTypeDef GPIO_InitStructure;    
	GPIO_InitStructure.GPIO_Mode = GPIO_Mode_Out_PP;
	GPIO_InitStructure.GPIO_Pin = GPIO_Pin_0;
	GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;			
    GPIO_Init(GPIOA,&GPIO_InitStructure);
 
    GPIO_SetBits(GPIOA,GPIO_Pin_0);
    PWM1_Init();
}
 
//ת̨
void Motor2_Start_U(void)
{
	    GPIO_SetBits(GPIOA, GPIO_Pin_3);
        PWM_SetCompare3(50);	
}

void Motor2_Start_D(void)
{
	    GPIO_ResetBits(GPIOA, GPIO_Pin_3);
        PWM_SetCompare3(50);
}

void Motor2_Stop(void)
{
	PWM_SetCompare3(0);
}

//���Ӵ�
void Motor3_Start_U(void)
{
	    GPIO_SetBits(GPIOA, GPIO_Pin_0);
        PWM_SetCompare2(50);	
}

void Motor3_Start_D(void)
{
	    GPIO_ResetBits(GPIOA, GPIO_Pin_0);
        PWM_SetCompare2(50);
}

void Motor3_Stop(void)
{
	PWM_SetCompare2(0);
}
