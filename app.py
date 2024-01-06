import matplotlib.pyplot as plt
import numpy as np
import math

from writer import write_results_to_csv


def main():
    """o main recebe um valor para a variavel sh (salario hora) e calcula todos os valores e
    graficos a partir deste parametro"""
    
    #Definição das variaveis usadas no codigo
    
    #var 1°funcao
    d=5   #mm  #950
    a=0.40   #mm/v
    la=300.0   #mm
    pi=math.pi
    #var 2°função
    ta=0.21
    ts=0.36   #min/p
    tp=25   #min
    z=800
    sh = 100 
    """aqui esta sh value responsavel pela criacao dos graficos"""
    sm = 150.0
    kft = 40
    mini = 0.1
    '''aqui o valor minimo do grafico, (ponto de origem)'''
    sizex = 10.0  
    '''aqui o valor maximo do grafico no eixo x'''
    res = 10000
    '''aqui a resolucao dos v values que serao a resolucao dos ponstos do grafico '''
    #var 3°funcao
    k=8.8*(10^6)
    x=2.71
    tft=3.60#min
    tfa=1.0

    #funçoes do codigo
    def ftc(d,pi,a,la,v):
        ''' função ftc recebe dimetro (d), numero pi(pi),avanço (a),percurso de avanço (la) e
        velocidade (v). A função determina o tempo da operação de corte de uma peça hipotética'''
        return(la*pi*d)/(1000*a*v)
    
    def ft1(ts,ta,tp,z):
        '''Funcão recebe tempo de troca (ts), tempo de afiação da peça(ta) tempo de preparo de 
        máquina(tp) e tamanho do lote (z). A função determina um tempo médio para parâmetros não 
        relacionados com a operação de usinagem.'''
        return(ts+ta+tp/z)
    
    def ft2(la, pi, d, v, a, k, z, tft, tfa):
        '''A função recebe percuso de avanço (la), numero pi (pi), diametro (d), velocidade (v),
        avanço (a), custo (k), tamanho do lote (z), tempo de troca de ferramenta(tft) e tempo de
        afiação de ferramenta(tfa). A função ft2 retorna  o tempo de troca e tempo de afiação de
        ferramenta'''
        return ((la * pi * d * (v**(x-1))) / (1000 * a * k) - 1/z) * (tft + tfa)
    
    def ftt(d,pi,a,la,v,ts,ta,tp,z, k, tft, tfa):
        '''A função recebe: diametro(d), numero pi (pi), avanço (a), percurso de avanço (la), 
        velocidade (v), tempo de troca (ts), tempo de afiação da peça (ta), tempo de preparo 
        de maquina (tp), tamanho de lote (z), custo (k), '''
        return ftc(d, pi, a, la, v) + ft1(ts, ta, tp, z) + ft2(la, pi, d, v, a, k, z, tft, tfa)
    
    def fc1():   #"Retorna custo de materia prima (cte)"
        return 6
    
    def c2(sh,sm):
        '''função recebe salário hora do operador (sh) e salário máquina (sm), retornando custo
        de valores que não dependem da velocidade de corte'''
        return(sh+sm)
    
    def c3(kft,tft,tfa,sm,sh):
        '''função recebe custo de tempo de troca de ferramenta (kft), tempo de troca de ferramenta
        (tft), tempo de afiação de ferramenta (tfa), salário máquina (sm) e salário hora (sh),
        retornando constante de custo relativo a ferramenta'''
        return (kft+((tft+tfa)/60)*(sh+sm))
    
    def fc2(a,pi,la,v,d,sh,sm):
        '''função recebe avanço (a), número pi (pi), percurso de avanço (la), velocidade (v), 
        diâmetro (d), salário hora(sh) e salário máquina (sm). Retorna soma das despesas 
        totais de mão de obra e salário máquina'''
        return ((pi*d*la)*c2(sh,sm)/(60*1000*a*v))
    
    def fc3(pi,d,la,v,x,k,kft,tft,tfa,sh,sm):
        '''função recebe número pi, diâmetro (d), percurso de avanço (la), velociade (v), x de 
        taylor (x), custo (k), custo de troca de ferramenta (kft), tempo de troca de ferramenta
        (tft), tempo de afiação de ferramenta (tfa), salário hora (sh) e salário máquina (sm).'''
        return((pi*d*la*(v**(x-1)))*c3(kft,tft,tfa,sh,sm)/(1000*a*k))
    
    def kp(a,pi,la,v,d,sh,sm,x,k,kft,tft,tfa):
        '''Função recebe avanço (a), número pi (pi), percurso de avanço (la), velocidade (v),
        diametro(d), salário hora(sh), salário máquina (sm), x de taylor (x), custo (k),  
        custo de tempo de troca de ferramenta (kft), tempo de troca de ferramenta(tft), tempo 
        de afiação de ferramenta (tfa)'''
        return (fc1()+fc2(a,pi,la,v,d,sh,sm)+fc3(pi,d,la,v,x,k,kft,tft,tfa,sh,sm))
    
    def vFunc(min,sizex,res):
        '''retornará uma lista dos pontos no eixo x para plotar'''
        return (np.linspace(min, sizex,res))
    v_values=vFunc(mini,sizex,res).tolist()
    
    
    #encontrando os pontos no eixo y para o primeiro grafico
    tc_values = [ftc(d,pi,a,la,v) for v in v_values]
    t1_values = [ft1(ts,ta,tp,z) for v in v_values]
    t2_values = [ft2(la,pi,d,v,a,k,z,tft,tfa) for v in v_values]
    tt_values = [ftt(d,pi,a,la,v,ts,ta,tp,z, k, tft, tfa) for v in v_values]
    
    #encontrando os pontos no eixo y para o segundo grafico
    c1_values = [fc1() for v in v_values]
    c2_values = [fc2(a,pi,la,v,d,sh,sm) for v in v_values]
    c3_values = [fc3(pi,d,la,v,x,k,kft,tft,tfa,sh,sm) for v in v_values]
    kp_values = [kp(a,pi,la,v,d,sh,sm,x,k,kft,tft,tfa) for v in v_values]
    
    #encontrando minimos 
    mintt=min(tt_values)
    locxtt=tt_values.index(mintt)
    minkp=min(kp_values)
    locxkp=kp_values.index(minkp)
    
    #área de plotagem de gráfico
    plt.figure(1)
    plt.plot(v_values,tc_values)
    plt.plot(v_values,t1_values)
    plt.plot(v_values,t2_values)
    plt.plot(v_values,tt_values)
    plt.title('Curva de tempo',fontsize=18)
    plt.xlabel('v (m/min)',fontsize=14)
    plt.ylabel('min',fontsize=14)
    plt.ylim(0,10)
    
    plt.figure(2)
    plt.plot(v_values,c1_values)
    plt.plot(v_values,c2_values)
    plt.plot(v_values,c3_values)
    plt.plot(v_values,kp_values)
    plt.title('Curva de custo',fontsize=18)
    plt.xlabel('v (m/min)',fontsize=14)
    plt.ylabel('R$/peça', fontsize=14)
    plt.legend(['c1', 'c2', 'c3','kp'])
    
    plt.figure(3)
    plt.plot(v_values,tt_values)
    plt.plot(v_values,kp_values)
    plt.scatter(v_values[locxtt], mintt, color='red', label='min tt', marker='o')
    plt.scatter(v_values[locxkp], minkp, color='blue', label='min kp', marker='o')
    plt.fill(
        [v_values[locxtt], v_values[locxkp], v_values[locxkp], v_values[locxtt]],
        [0, 0, minkp, minkp],
        color='red', alpha=0.5
    )
    plt.title('Curva do intervalo',fontsize=18)
    plt.xlabel('v (m/min)',fontsize=14)
    plt.ylabel('tempo e R$',fontsize=14)
    plt.legend(['tt', 'kp','minimo tt','minimo kt','área de eficiência'])
    plt.show()
    df = write_results_to_csv(
        sh,
        v_values,
        tc_values,
        t1_values,
        t2_values,
        tt_values,
        c1_values,
        c2_values,
        c3_values,
        kp_values
    )

    # result = df.describe()

    # tt_min = result['tt_values']['min'] 
    # kp_min = result['kp_values']['min']

    # tt_min_x = get_v_value(df, 'tt_values', tt_min, 'v_values')['tt_values']
    # kp_min_x = get_v_value(df, 'kp_values', kp_min, 'v_values')['kp_values']


if __name__ == "__main__":
    main()