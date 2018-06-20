players = read.csv("listPlayers.csv")
attach(players)
tabelaTiers <- table(tier,rank)
barplot(tabelaTiers, legend.text = T,col = c(1,2,3,4,5))
barplot(tabelaTiers, legend.text = T,space = 1,  col = c(1,2,3,4,5), horiz = 1,angle = 10)

agregado <- aggregate(visionScore, list(tier),mean)
barplot(agregado$x, names.arg = agregado$Group.1,main = "Média de Vision Score",col = c(1,3,2,1,8,7,4))


dataFramePlayers$ordem <-  factor(agregado$Group.1,levels = c("BRONZE","SILVER","GOLD","PLATINUM","DIAMOND","MASTER","CHALLENGER"))
mediaFarmTierLanewin <- aggregate(partidas$minion,list(partidas$tier,partidas$role,partidas$win),mean)


partidasKill <- read.csv("saidaKill.csv")
partidasKill$ordem <- factor(partidasKill$tier,levels = c("BRONZE","SILVER","GOLD","PLATINUM","DIAMOND","MASTER","CHALLENGER"))




table( (partidas$visionScore > agregadoMediaVision$x[which(agregadoMediaVision$Group.1 == partidas$tier & agregadoMediaVision$Group.2 == partidas$role)]) ,partidas$win)


tabelaPlayers <- table(players$rank,players$tier)
dataFramePlayers <- as.data.frame.matrix(tabelaPlayers)

gregado3 <- aggregate(partidaAssist$kdRatio,list(partidaAssist$tier,partidaAssist$ordem),mean)

ggplot(agregado,aes(x = agregado$teste,y = agregado$x)) + geom_bar(stat = "identity",aes(fill = agregado$Group.1 )) + labs(x="Tier", y = "Média de KD ratio")teste <-  function(tabela){

agregado$teste = factor(agregado$Group.1,levels = c("BRONZE","SILVER","GOLD","PLATINUM","DIAMOND","MASTER","CHALLENGER"))
  
ggplot(agregado,aes(x = agregado$teste,y = agregado$x)) + geom_bar(stat = "identity",aes(fill = agregado$Group.1 )) + labs(x="Tier", y = "Média de KD ratio") + labs(colour = "teste") + guides(fill = guide_legend(title = "Tier")) + ggtitle("Average Kill per Death")

ggplot(agregado3,aes(x = agregado3$teste,y = agregado3$x)) + geom_bar(stat = "identity",aes(fill = agregado3$Group.1 )) + labs(x="Tier", y = "Média de Assist/Death") + labs(colour = "teste") + guides(fill = guide_legend(title = "Tier") ) + ggtitle("Average Assist per Death")

ggplot(partidas2,aes(x = partidas2$teste,y = partidas2$kdRatio,color=partidas2$role)) + geom_boxplot() + labs(colour = "Role") + labs(x="Tier",y = "K/D") + ggtitle("K/D per Tier and Role")

ggplot(partidaCombinada,aes(x = partidaCombinada$ordem,y = partidaCombinada$kdRatio,color=partidaCombinada$role)) + geom_boxplot() + labs(colour = "Role") + labs(x="Tier",y = "K/D") + ggtitle("(K + A)/D per Tier and Role")