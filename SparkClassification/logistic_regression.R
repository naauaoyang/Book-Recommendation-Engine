boolean_v<-read.csv("~/Downloads/boolean_v.csv")
boolean_v<-boolean_v$Helpful
boolean_v<-as.data.frame(boolean_v)
pos_neg<-read.csv("~/Downloads/pos_neg_v.csv")
lengthw<-read.csv("~/Downloads/avg_length.csv")
length<-read.csv("~/Downloads/length_v.csv")
rating<-read.csv("~/Downloads/rating_v.csv")
nrow(rating)
nrow(length)
length<-length[1:705205,]
rating<-rating[1:705205,]
rating<-as.data.frame(rating)
#avg_length<-ifelse(lengthw==0,0,length/lengthw)
#avg_length<-as.data.frame(avg_length)
#nrow(avg_length)
glm.fit=glm(boolean_v$boolean_v~pos_neg$pos_neg+lengthw$lengthw+lengthw$avg_length+rating$rating,family=binomial)
summary(glm.fit)
contrasts(boolean_v$boolean_v)
glm.probs=predict(glm.fit,type="response")
glm.pred=rep("unhelpful",705205)
glm.pred[glm.probs<.5]="helpful"
table(glm.pred,boolean_v$boolean_v)
mean(glm.pred==boolean_v$boolean_v)

smp_size <- floor(0.75 * nrow(boolean_v))
set.seed(123)
train_ind <- sample(seq_len(nrow(boolean_v)), size = smp_size)
train_boolean_v <- boolean_v[train_ind, ]
test_boolean_v <- boolean_v[-train_ind, ]
train_pos_neg<-pos_neg[train_ind, ]
test_pos_neg<-pos_neg[-train_ind, ]
train_lengthw<-lengthw[train_ind, ]
test_lengthw<-lengthw[-train_ind, ]
train_rating<-rating[train_ind, ]
test_rating<-rating[-train_ind, ]
X<-cbind(train_boolean_v,train_pos_neg,train_lengthw,train_rating)
X_test<-cbind(test_boolean_v,test_pos_neg,test_lengthw,test_rating)
colnames(X)<-c("boolean_v","pos_neg","lengthw","avg_length","rating")
colnames(X_test)<-c("boolean_v","pos_neg","lengthw","avg_length","rating")
glm.fit=glm(boolean_v~pos_neg+lengthw+avg_length+rating,data=X,family=binomial)
nrow(X_test)
contrasts(X_test$test_boolean_v)
glm.pred=rep("unhelpful",176302)
glm.probs=predict(glm.fit,X_test,type="response")
glm.pred[glm.probs<.5]="helpful"
table(glm.pred,X_test$boolean_v)
mean(glm.pred==X_test$boolean_v)
summary(glm.fit)

True_Label <- factor(c("helpful", "helpful", "unhelpful", "unhelpful"))
Predicted_Label <- factor(c("helpful", "unhelpful", "helpful", "unhelpful"))
Y <- c(round(37012/(42430+37012),2), round(42430/(42430+37012),2), round(19279/(77581+19279),2), round(77581/(77581+19279),2))
df <- data.frame(True_Label, Predicted_Label, Y)

library(ggplot2)
plotx<-ggplot(data =  df, mapping = aes(x = True_Label, y = Predicted_Label)) +
  geom_tile(aes(fill = Y), colour = "white") +
  geom_text(aes(label = Y), vjust = 1,color="white") +
  scale_fill_gradient(low = "grey", high = "black") +
  theme_bw() + theme(legend.position = "none")

plotx + ggtitle("Confusion Matrix")

library("ROCR")
predvec <- ifelse(glm.pred=="helpful", 1, 0)
realvec <- ifelse(X_test$boolean_v=="helpful", 1, 0)
pred <- prediction(predvec, realvec)
perf <- performance(pred,"tpr","fpr")
par(mar=c(5,5,2,2),xaxs = "i",yaxs = "i",cex.axis=1.3,cex.lab=1.4)
plot(perf,col="black",lty=3, lwd=3)
