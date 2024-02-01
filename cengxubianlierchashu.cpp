//
// Created by fyz on 2024/2/1.
//
#include <iostream>
using namespace std;
int sum=0;
struct ElemType{
    int value;
};
typedef struct BiTNode{
    ElemType value;
    struct BiTNode*lchild,*rchild;
}BiTNode,*BiTree;
typedef struct LinkNode{
    BiTree data;
    struct LinkNode*next;
}LinkNode;
typedef struct LinkQueue{
    struct LinkNode*front,*rear;
}LinkQueue;
void visit(BiTree p){
    sum+=p->value.value;
}
void InitQueue(LinkQueue &Q){
    Q.front=Q.rear=(LinkNode*) malloc(sizeof(LinkNode));
}
bool isEmpty(LinkQueue Q){
    if(Q.rear==Q.front)return true;
    else return false;
}
void EnQueue(LinkQueue &Q,BiTree p){
    LinkNode *s=(LinkNode*) malloc(sizeof(LinkNode));
    s->data=p;
    s->next= nullptr;
    Q.rear->next=s;
    Q.rear=s;
}
bool DeQueue(LinkQueue &Q,BiTree &p){
    if(Q.rear==Q.front)return false;
    LinkNode *s=Q.front->next;
    p=s->data;
    Q.front->next=s->next;
    if(s==Q.rear)Q.rear=Q.front;
    free(s);
    return true;
}

int main(){
    BiTree root=(BiTree)malloc(sizeof(BiTNode));
    root->value={1};
    root->lchild=(BiTree)malloc(sizeof(BiTNode));
    root->rchild=(BiTree)malloc(sizeof(BiTNode));
    root->lchild->value={2};
    root->rchild->value={3};
    root->lchild->lchild=(BiTree)malloc(sizeof(BiTNode));     //    1
    root->lchild->rchild=(BiTree)malloc(sizeof(BiTNode));//       2   3
    root->lchild->lchild->value={4};//                         4  5 6
    root->lchild->lchild->lchild= nullptr;
    root->lchild->lchild->rchild= nullptr;
    root->lchild->rchild->value={5};
    root->lchild->rchild->lchild= nullptr;
    root->lchild->rchild->rchild= nullptr;
    root->rchild->lchild=(BiTree)malloc(sizeof(BiTNode));
    root->rchild->rchild= nullptr;
    root->rchild->lchild->value={6};
    root->rchild->lchild->lchild= nullptr;
    root->rchild->lchild->rchild= nullptr;
    LinkQueue Q;
    InitQueue(Q);
    EnQueue(Q,root);
    while(!isEmpty(Q)){
        DeQueue(Q,root);
        visit(root);
        if(root->lchild)EnQueue(Q,root->lchild);
        if(root->rchild)EnQueue(Q,root->rchild);
    }
    cout<<sum;
}